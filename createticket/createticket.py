import discord
from redbot.core import commands, app_commands
import json
import os
import requests
import aiohttp

class FreshdeskCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()
        self.role_config_file = os.path.join(os.path.dirname(__file__), "roles_config.json")
        self.load_roles()

    def load_roles(self):
        try:
            with open(self.role_config_file, "r") as f:
                self.allowed_roles = json.load(f)
        except FileNotFoundError:
            self.allowed_roles = {}

    def save_roles(self):
        with open(self.role_config_file, "w") as f:
            json.dump(self.allowed_roles, f)

    @commands.command()
    async def create_ticket(self, ctx):
        await ctx.send("Let's create a Freshdesk ticket. Please provide the following information.")

        def check(message):
            return message.author == ctx.message.author

        ticket_data = {}
        ticket_data["ticketid"] = ctx.message.id  # You can use a unique identifier for ticket ID
        await ctx.send("Please enter the Title of your ticket:")
        description = await self.bot.wait_for('message', check=check)
        ticket_data["description"] = description.content

        await ctx.send("Please enter the reason:")
        subject = await self.bot.wait_for('message', check=check)
        ticket_data["subject"] = subject.content

        await ctx.send("Please enter the email:")
        email = await self.bot.wait_for('message', check=check)
        ticket_data["email"] = email.content

        ticket_data["status"] = 2
        ticket_data["priority"] = 1

        # Send the data to Freshdesk via the API
        freshdesk_api_key = 'MoTybUBrM61tkY06mbNH'
        freshdesk_domain = 'dreamsport'
        freshdesk_api_url = f'https://{freshdesk_domain}.freshdesk.com/api/v2/tickets'

        headers = {
            'Content-Type': 'application/json',
        }
        auth = (freshdesk_api_key, 'X')

        response = requests.post(freshdesk_api_url, data=json.dumps(ticket_data), headers=headers, auth=auth)

        if response.status_code == 201:
            await ctx.send("Ticket created successfully")
        else:
            await ctx.send(f"Failed to create the ticket. Status code: {response.status_code}")