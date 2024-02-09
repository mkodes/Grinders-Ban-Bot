# Discord VoteBan Bot

## Description
This bot allows members of a Discord server to vote on banning a member. A vote is initiated by a member with a specific role, and the community can vote by reacting to the bot's message. If the majority votes for the ban within the time limit, the bot will execute the ban.

## Features
- Slash command `/voteban` to initiate a vote.
- Customizable role check to restrict who can initiate votes.
- Majority vote decides the action.
- Configurable time limit for voting.

## Setup
1. **Clone the repository**
   git clone https://github.com/yourgithubusername/discord-voteban-bot.git
   
2. **Install dependencies**
pip install -r requirements.txt

3. **Configuration**
- Replace `your-bot-token` with your Discord bot token.
- Set `YOUR_GUILD_ID_HERE` to your server's ID.
- Set `YOUR_MEMBER_ROLE_ID_HERE` to the role ID allowed to initiate votes.
4. **Run the bot**
python bot.py


## Usage
- Use the `/voteban` command followed by the member to ban and the reason.
- Vote using 👍 or 👎 reactions.
- The bot will announce the decision after the voting period.

## Contributing
Contributions are welcome! Please feel free to submit pull requests or open issues to improve the bot.

## License
Distributed under the MIT License. See `LICENSE` for more information.



