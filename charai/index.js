const CharacterAI = require('node_characterai');
const characterAI = new CharacterAI();

const prompt = require('prompt-sync')();

(async() => {
    await characterAI.authenticateAsGuest();

    // const characterId = "8_1NyR8w1dOXmI1uWaieQcd147hecbdIK7CeEAIrdJw" // Discord moderator
    const characterId = "yVso4c2Co_gZNovdIdqu3efLNJ_n6U2R5PXiMF44tbc" // Discord moderator

    const chat = await characterAI.createOrContinueChat(characterId);

    while(1) {
        const msg = prompt('> ');
        if(msg == 'q')
            break;
        const response = await chat.sendAndAwaitResponse(msg, true);
        console.log(response.text);
        await fetch('http://localhost:6969/', {
            method: 'POST',
            body: response.text
        })
    }

})();