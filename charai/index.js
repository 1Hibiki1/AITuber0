/* character AI API */
const CharacterAI = require('node_characterai');
const characterAI = new CharacterAI();

/* for user input */
const prompt = require('prompt-sync')();

/* change this for diferent character */
const characterId = "yVso4c2Co_gZNovdIdqu3efLNJ_n6U2R5PXiMF44tbc";

/* tts server params */
const tts_server_base_url = "http://127.0.0.1";
const tts_server_port = "6969";
const tts_server_route = "/";

(async() => {
    await characterAI.authenticateAsGuest();
    const chat = await characterAI.createOrContinueChat(characterId);

    console.log("type 'q' to exit :)");

    while(1) {
        const msg = prompt('> ');

        /* quit if user enters 'q' */
        if(msg == 'q')
            break;

        /* get message response */
        const response = await chat.sendAndAwaitResponse(msg, true);

        /* print response */
        console.log("\n");
        console.log(response.text);
        console.log("\n");

        /* send message to tts server */
        await fetch(`${tts_server_base_url}:${tts_server_port}${tts_server_route}`, {
            method: 'POST',
            body: response.text
        });
    }

})();