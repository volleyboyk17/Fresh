/**
 * Random JavaScript Program: Number Guessing Game
 * A fun interactive game where players try to guess a random number
 * Features: Multiple difficulty levels, score tracking, and game statistics
 */

class NumberGuessingGame {
    constructor() {
        this.score = 0;
        this.gamesPlayed = 0;
        this.totalGuesses = 0;
        this.bestScore = Infinity;
        this.difficulty = 'medium';
        this.ranges = {
            easy: { min: 1, max: 50, maxGuesses: 10 },
            medium: { min: 1, max: 100, maxGuesses: 7 },
            hard: { min: 1, max: 200, maxGuesses: 5 }
        };
        this.currentGame = null;
    }

    setDifficulty(level) {
        if (this.ranges[level]) {
            this.difficulty = level;
            console.log(`🎯 Difficulty set to: ${level.toUpperCase()}`);
            this.displayDifficultyInfo();
        } else {
            console.log('❌ Invalid difficulty! Choose: easy, medium, or hard');
        }
    }

    displayDifficultyInfo() {
        const range = this.ranges[this.difficulty];
        console.log(`📊 Range: ${range.min}-${range.max}, Max Guesses: ${range.maxGuesses}`);
    }

    startNewGame() {
        const range = this.ranges[this.difficulty];
        this.currentGame = {
            targetNumber: Math.floor(Math.random() * (range.max - range.min + 1)) + range.min,
            guesses: 0,
            maxGuesses: range.maxGuesses,
            gameOver: false,
            won: false
        };

        console.log('\n🎮 NEW GAME STARTED!');
        console.log(`🎲 I'm thinking of a number between ${range.min} and ${range.max}`);
        console.log(`🎯 You have ${range.maxGuesses} guesses to find it!`);
        console.log('💡 Use game.guess(number) to make a guess');
    }

    guess(number) {
        if (!this.currentGame) {
            console.log('❌ No active game! Use game.startNewGame() first');
            return;
        }

        if (this.currentGame.gameOver) {
            console.log('🏁 Game is over! Start a new game with game.startNewGame()');
            return;
        }

        if (typeof number !== 'number' || number < 1) {
            console.log('❌ Please enter a valid positive number');
            return;
        }

        this.currentGame.guesses++;
        const remaining = this.currentGame.maxGuesses - this.currentGame.guesses;

        if (number === this.currentGame.targetNumber) {
            this.currentGame.won = true;
            this.currentGame.gameOver = true;
            this.updateStats();
            this.displayWinMessage();
        } else if (this.currentGame.guesses >= this.currentGame.maxGuesses) {
            this.currentGame.gameOver = true;
            this.updateStats();
            this.displayLoseMessage();
        } else {
            this.provideHint(number, remaining);
        }
    }

    provideHint(guess, remaining) {
        const target = this.currentGame.targetNumber;
        const difference = Math.abs(guess - target);
        
        let direction = guess < target ? '📈 Higher!' : '📉 Lower!';
        let temperature = '';
        
        if (difference <= 5) temperature = '🔥 Very Hot!';
        else if (difference <= 15) temperature = '🌡️ Hot!';
        else if (difference <= 30) temperature = '❄️ Cold!';
        else temperature = '🧊 Very Cold!';

        console.log(`${direction} ${temperature} (${remaining} guesses left)`);
    }

    displayWinMessage() {
        const guesses = this.currentGame.guesses;
        console.log('\n🎉 CONGRATULATIONS! YOU WON! 🎉');
        console.log(`🎯 You found ${this.currentGame.targetNumber} in ${guesses} guesses!`);
        
        if (guesses === 1) console.log('🏆 INCREDIBLE! First try!');
        else if (guesses <= 3) console.log('⭐ EXCELLENT! Amazing guessing!');
        else if (guesses <= 5) console.log('👍 GOOD JOB! Well done!');
        else console.log('✅ SUCCESS! You made it!');
    }

    displayLoseMessage() {
        console.log('\n💔 GAME OVER! You ran out of guesses!');
        console.log(`🎯 The number was: ${this.currentGame.targetNumber}`);
        console.log('🔄 Better luck next time!');
    }

    updateStats() {
        this.gamesPlayed++;
        this.totalGuesses += this.currentGame.guesses;
        
        if (this.currentGame.won) {
            this.score++;
            if (this.currentGame.guesses < this.bestScore) {
                this.bestScore = this.currentGame.guesses;
                console.log('🏆 NEW BEST SCORE!');
            }
        }
    }

    showStats() {
        console.log('\n📊 GAME STATISTICS');
        console.log('═'.repeat(30));
        console.log(`🎮 Games Played: ${this.gamesPlayed}`);
        console.log(`🏆 Games Won: ${this.score}`);
        console.log(`📈 Win Rate: ${this.gamesPlayed > 0 ? ((this.score / this.gamesPlayed) * 100).toFixed(1) : 0}%`);
        console.log(`🎯 Average Guesses: ${this.gamesPlayed > 0 ? (this.totalGuesses / this.gamesPlayed).toFixed(1) : 0}`);
        console.log(`⭐ Best Score: ${this.bestScore === Infinity ? 'N/A' : this.bestScore} guesses`);
        console.log(`🎲 Current Difficulty: ${this.difficulty.toUpperCase()}`);
    }

    showHelp() {
        console.log('\n🎮 GAME COMMANDS');
        console.log('═'.repeat(40));
        console.log('🆕 game.startNewGame()     - Start a new game');
        console.log('🎯 game.guess(number)      - Make a guess');
        console.log('⚙️  game.setDifficulty()   - Change difficulty (easy/medium/hard)');
        console.log('📊 game.showStats()        - View your statistics');
        console.log('❓ game.showHelp()         - Show this help menu');
        console.log('\n🎲 Difficulty Levels:');
        Object.entries(this.ranges).forEach(([level, info]) => {
            console.log(`   ${level.toUpperCase()}: ${info.min}-${info.max} (${info.maxGuesses} guesses)`);
        });
    }

    // Bonus: Auto-play demo function
    autoPlay() {
        console.log('\n🤖 AUTO-PLAY DEMO');
        this.startNewGame();
        
        const range = this.ranges[this.difficulty];
        let low = range.min;
        let high = range.max;
        
        const autoGuess = () => {
            if (this.currentGame.gameOver) return;
            
            const guess = Math.floor((low + high) / 2);
            console.log(`🤖 Bot guesses: ${guess}`);
            
            const originalTarget = this.currentGame.targetNumber;
            this.guess(guess);
            
            if (!this.currentGame.gameOver) {
                if (guess < originalTarget) {
                    low = guess + 1;
                } else {
                    high = guess - 1;
                }
                setTimeout(autoGuess, 1000);
            }
        };
        
        setTimeout(autoGuess, 500);
    }
}

// Initialize the game
const game = new NumberGuessingGame();

// Welcome message
console.log('🎮 Welcome to the Number Guessing Game!');
console.log('═'.repeat(50));
console.log('🎯 Try to guess the secret number!');
console.log('💡 Type game.showHelp() for commands');
console.log('🚀 Type game.startNewGame() to begin!');

// Export for potential module use
if (typeof module !== 'undefined' && module.exports) {
    module.exports = NumberGuessingGame;
}
