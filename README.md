# 🎮 Number Guessing Game

A fun and interactive JavaScript program that challenges players to guess a randomly generated number!

## 🚀 Features

- **Multiple Difficulty Levels**: Easy (1-50), Medium (1-100), Hard (1-200)
- **Smart Hints**: Get "hot/cold" feedback and directional hints
- **Statistics Tracking**: Win rate, average guesses, best score
- **Auto-Play Demo**: Watch an AI solve the puzzle using binary search
- **Browser & Node.js Compatible**: Works in both environments

## 🎯 How to Play

### Command Line (Node.js)
```bash
node number-guessing-game.js
```

Then use these commands:
- `game.startNewGame()` - Start a new game
- `game.guess(42)` - Make a guess
- `game.setDifficulty('easy')` - Change difficulty
- `game.showStats()` - View your statistics
- `game.showHelp()` - Show all commands
- `game.autoPlay()` - Watch AI play

### Browser
Open `game-demo.html` in your web browser for a beautiful GUI version with buttons and visual feedback!

## 🎲 Difficulty Levels

| Level | Range | Max Guesses |
|-------|-------|-------------|
| Easy | 1-50 | 10 |
| Medium | 1-100 | 7 |
| Hard | 1-200 | 5 |

## 🏆 Game Features

- **Smart Feedback**: Get temperature hints (🔥 Very Hot, ❄️ Cold, etc.)
- **Achievement System**: Special messages for different performance levels
- **Statistics**: Track your progress over multiple games
- **Binary Search Demo**: Watch optimal AI gameplay

## 📊 Example Gameplay

```
🎮 NEW GAME STARTED!
🎲 I'm thinking of a number between 1 and 100
🎯 You have 7 guesses to find it!

> game.guess(50)
📈 Higher! ❄️ Cold! (6 guesses left)

> game.guess(75)
📉 Lower! 🌡️ Hot! (5 guesses left)

> game.guess(68)
🎉 CONGRATULATIONS! YOU WON! 🎉
🎯 You found 68 in 3 guesses!
⭐ EXCELLENT! Amazing guessing!
```

Enjoy the game! 🎉
