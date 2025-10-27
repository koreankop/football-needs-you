// Game State
let goals = 0;
let attempts = 0;

// DOM Elements
const goalsElement = document.getElementById('goals');
const attemptsElement = document.getElementById('attempts');
const successRateElement = document.getElementById('success-rate');
const resultMessage = document.getElementById('result-message');
const goalkeeper = document.getElementById('goalkeeper');
const ball = document.getElementById('ball');
const resetButton = document.getElementById('reset-button');
const goalSections = document.querySelectorAll('.goal-section');

// Game Logic
function shoot(playerDirection) {
    // Disable goal sections during animation
    disableGoalSections();

    // Increment attempts
    attempts++;
    updateScoreboard();

    // Goalkeeper randomly chooses a direction
    const directions = ['left', 'center', 'right'];
    const keeperDirection = directions[Math.floor(Math.random() * directions.length)];

    // Animate ball
    ball.classList.add(`shoot-${playerDirection}`);

    // Animate goalkeeper
    goalkeeper.classList.add(`dive-${keeperDirection}`);

    // Determine result
    setTimeout(() => {
        const isGoal = playerDirection !== keeperDirection;

        if (isGoal) {
            goals++;
            showResult('GOAL! ⚽🎉', 'goal');
        } else {
            showResult('SAVED! 🧤', 'save');
        }

        updateScoreboard();

        // Reset animations after a delay
        setTimeout(() => {
            resetAnimations();
            enableGoalSections();
        }, 1500);
    }, 600);
}

function disableGoalSections() {
    goalSections.forEach(section => {
        section.classList.add('disabled');
    });
}

function enableGoalSections() {
    goalSections.forEach(section => {
        section.classList.remove('disabled');
    });
}

function resetAnimations() {
    // Remove ball animations
    ball.classList.remove('shoot-left', 'shoot-center', 'shoot-right');

    // Remove goalkeeper animations
    goalkeeper.classList.remove('dive-left', 'dive-center', 'dive-right');

    // Clear result message
    resultMessage.textContent = '';
    resultMessage.classList.remove('goal', 'save');
}

function showResult(message, type) {
    resultMessage.textContent = message;
    resultMessage.className = 'result-message ' + type;
}

function updateScoreboard() {
    goalsElement.textContent = goals;
    attemptsElement.textContent = attempts;

    const successRate = attempts > 0 ? Math.round((goals / attempts) * 100) : 0;
    successRateElement.textContent = successRate + '%';
}

function resetScore() {
    goals = 0;
    attempts = 0;
    updateScoreboard();
    resetAnimations();

    // Show reset confirmation
    showResult('Score Reset! Ready for a new game? 🔄', 'goal');
    setTimeout(() => {
        resultMessage.textContent = '';
        resultMessage.className = 'result-message';
    }, 2000);
}

// Event Listeners
goalSections.forEach(section => {
    section.addEventListener('click', (e) => {
        const direction = e.currentTarget.getAttribute('data-direction');
        shoot(direction);
    });
});

resetButton.addEventListener('click', resetScore);

// Initialize
updateScoreboard();

// Add keyboard support
document.addEventListener('keydown', (e) => {
    if (document.querySelector('.goal-section.disabled')) {
        return; // Don't allow keyboard input during animation
    }

    switch(e.key.toLowerCase()) {
        case 'a':
        case 'arrowleft':
            shoot('left');
            break;
        case 's':
        case 'arrowdown':
            shoot('center');
            break;
        case 'd':
        case 'arrowright':
            shoot('right');
            break;
    }
});

// Add welcome message
console.log('⚽ Football Needs You! ⚽');
console.log('Click on a goal section to shoot!');
console.log('Or use keyboard controls:');
console.log('  A or Left Arrow = Shoot Left');
console.log('  S or Down Arrow = Shoot Center');
console.log('  D or Right Arrow = Shoot Right');
console.log('Good luck! 🍀');
