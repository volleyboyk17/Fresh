// English to Tamil translation dictionary
const translationDictionary = {
    // Common words and phrases
    'hello': 'வணக்கம்',
    'hi': 'வணக்கம்',
    'good morning': 'காலை வணக்கம்',
    'good evening': 'மாலை வணக்கம்',
    'good night': 'இனிய இரவு',
    'thank you': 'நன்றி',
    'thanks': 'நன்றி',
    'please': 'தயவுசெய்து',
    'sorry': 'மன்னிக்கவும்',
    'excuse me': 'மன்னிக்கவும்',
    'yes': 'ஆம்',
    'no': 'இல்லை',
    'okay': 'சரி',
    'ok': 'சரி',
    'welcome': 'வரவேற்கிறோம்',
    'goodbye': 'பிரியாவிடை',
    'bye': 'பிரியாவிடை',
    
    // Family
    'mother': 'அம்மா',
    'father': 'அப்பா',
    'brother': 'அண்ணன்',
    'sister': 'அக்காள்',
    'son': 'மகன்',
    'daughter': 'மகள்',
    'family': 'குடும்பம்',
    'grandmother': 'பாட்டி',
    'grandfather': 'தாத்தா',
    
    // Numbers
    'one': 'ஒன்று',
    'two': 'இரண்டு',
    'three': 'மூன்று',
    'four': 'நான்கு',
    'five': 'ஐந்து',
    'six': 'ஆறு',
    'seven': 'ஏழு',
    'eight': 'எட்டு',
    'nine': 'ஒன்பது',
    'ten': 'பத்து',
    
    // Colors
    'red': 'சிவப்பு',
    'blue': 'நீலம்',
    'green': 'பச்சை',
    'yellow': 'மஞ்சள்',
    'black': 'கருப்பு',
    'white': 'வெள்ளை',
    'orange': 'ஆரஞ்சு',
    'purple': 'ஊதா',
    'pink': 'இளஞ்சிவப்பு',
    'brown': 'பழுப்பு',
    
    // Food
    'food': 'உணவு',
    'water': 'தண்ணீர்',
    'rice': 'சாதம்',
    'bread': 'ரொட்டி',
    'milk': 'பால்',
    'tea': 'தேநீர்',
    'coffee': 'காபி',
    'fruit': 'பழம்',
    'vegetable': 'காய்கறி',
    'fish': 'மீன்',
    'chicken': 'கோழி',
    'egg': 'முட்டை',
    
    // Common verbs
    'eat': 'சாப்பிடு',
    'drink': 'குடி',
    'sleep': 'தூங்கு',
    'walk': 'நட',
    'run': 'ஓடு',
    'sit': 'உட்கார்',
    'stand': 'நில்',
    'come': 'வா',
    'go': 'போ',
    'see': 'பார்',
    'hear': 'கேள்',
    'speak': 'பேசு',
    'read': 'படி',
    'write': 'எழுது',
    'learn': 'கற்று',
    'teach': 'கற்பி',
    'work': 'வேலை',
    'play': 'விளையாடு',
    'love': 'காதல்',
    'like': 'பிடிக்கும்',
    
    // Time
    'time': 'நேரம்',
    'day': 'நாள்',
    'night': 'இரவு',
    'morning': 'காலை',
    'evening': 'மாலை',
    'today': 'இன்று',
    'tomorrow': 'நாளை',
    'yesterday': 'நேற்று',
    'week': 'வாரம்',
    'month': 'மாதம்',
    'year': 'வருடம்',
    
    // Places
    'home': 'வீடு',
    'school': 'பள்ளி',
    'hospital': 'மருத்துவமனை',
    'market': 'சந்தை',
    'temple': 'கோவில்',
    'city': 'நகரம்',
    'village': 'கிராமம்',
    'country': 'நாடு',
    'world': 'உலகம்',
    
    // Common phrases
    'how are you': 'எப்படி இருக்கிறீர்கள்',
    'what is your name': 'உங்கள் பெயர் என்ன',
    'my name is': 'என் பெயர்',
    'nice to meet you': 'உங்களை சந்தித்ததில் மகிழ்ச்சி',
    'i love you': 'நான் உன்னை காதலிக்கிறேன்',
    'i am fine': 'நான் நலமாக இருக்கிறேன்',
    'where are you from': 'நீங்கள் எங்கிருந்து வருகிறீர்கள்',
    'how much': 'எவ்வளவு',
    'what time': 'என்ன நேரம்',
    'i dont understand': 'எனக்கு புரியவில்லை',
    'can you help me': 'நீங்கள் எனக்கு உதவ முடியுமா',
    'i am hungry': 'எனக்கு பசிக்கிறது',
    'i am thirsty': 'எனக்கு தாகமாக இருக்கிறது',
    'where is': 'எங்கே இருக்கிறது',
    'how old are you': 'உங்கள் வயது என்ன'
};

// Function to translate text
function translateText() {
    const inputText = document.getElementById('english-input').value.trim();
    const outputElement = document.getElementById('tamil-output');
    const translateBtn = document.getElementById('translate-btn');
    
    if (!inputText) {
        alert('Please enter some English text to translate!');
        return;
    }
    
    // Show loading state
    translateBtn.disabled = true;
    translateBtn.innerHTML = '⏳ Translating...';
    outputElement.value = 'Translating...';
    
    // Simulate translation delay for better UX
    setTimeout(() => {
        const translation = performTranslation(inputText);
        outputElement.value = translation;
        
        // Reset button state
        translateBtn.disabled = false;
        translateBtn.innerHTML = '🔄 Translate';
    }, 800);
}

// Function to perform the actual translation
function performTranslation(text) {
    const lowerText = text.toLowerCase();
    
    // First, try to find exact phrase matches
    for (const [english, tamil] of Object.entries(translationDictionary)) {
        if (lowerText === english) {
            return tamil;
        }
    }
    
    // If no exact match, try to translate word by word
    const words = lowerText.split(/\s+/);
    const translatedWords = [];
    
    for (const word of words) {
        // Remove punctuation for matching
        const cleanWord = word.replace(/[^\w\s]/g, '');
        
        if (translationDictionary[cleanWord]) {
            translatedWords.push(translationDictionary[cleanWord]);
        } else {
            // If word not found, keep original word with a note
            translatedWords.push(`[${word}]`);
        }
    }
    
    let result = translatedWords.join(' ');
    
    // If no translations were found
    if (result === text || !result.includes('்') && !result.includes('ா') && !result.includes('ி')) {
        result += '\n\n📝 Note: Some words may not be in our dictionary. This is a basic translator with common Tamil words and phrases.';
    }
    
    return result;
}

// Add Enter key support for translation
document.getElementById('english-input').addEventListener('keypress', function(event) {
    if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault();
        translateText();
    }
});

// Add some sample text on page load
document.addEventListener('DOMContentLoaded', function() {
    const sampleTexts = [
        'hello',
        'thank you',
        'good morning',
        'how are you',
        'i love you'
    ];
    
    const randomSample = sampleTexts[Math.floor(Math.random() * sampleTexts.length)];
    document.getElementById('english-input').placeholder = `Try typing: "${randomSample}"`;
});

// Clear function (optional feature)
function clearText() {
    document.getElementById('english-input').value = '';
    document.getElementById('tamil-output').value = '';
    document.getElementById('english-input').focus();
}

// Add keyboard shortcut for clearing (Ctrl+L)
document.addEventListener('keydown', function(event) {
    if (event.ctrlKey && event.key === 'l') {
        event.preventDefault();
        clearText();
    }
});
