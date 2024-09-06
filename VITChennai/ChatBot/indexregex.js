document.addEventListener("DOMContentLoaded", () => {
    const inputField = document.getElementById("input");
    inputField.addEventListener("keydown", (e) => {
      if (e.code === "Enter") {
        let input = inputField.value;
        inputField.value = "";
        output(input);
      }
    });
  });
  
  function output(input) {
    let product;
  
    // Regex remove non word/space chars
    // Trim trailing whitespce
    // Remove digits - not sure if this is best
    // But solves problem of entering something like 'hi1'
  
    let text = input.toLowerCase().replace(/[^\w\s]/gi, "").replace(/[\d]/gi, "").trim();
    text = text
      .replace(/ a /g, " ")
      .replace(/i feel /g, "")
      .replace(/whats/g, "what is")
      .replace(/please /g, "")
      .replace(/ please/g, "")
      .replace(/r u/g, "are you");
  
    if ((match = compareWithSimilarity(prompts, replies, text))) { 
      // Search for exact match in `prompts`
      product = match;
    } else if ((match = compareWithSimilarity(earthprompts, earthreplies, text))) { 
      // Search for exact match in `earthprompts`
      product = match;
    } else if (text.match(/thank/gi)) {
      product = "You're welcome!"
    } else {
      // If all else fails: random alternative
      product = alternative[Math.floor(Math.random() * alternative.length)];
    }
  
    // Update DOM
    addChat(input, product);
  }

  //Adding a similaritycomparison with regex
  
  function stringSimilarity(str1, str2) {
    // Simple similarity calculation based on common words
    const words1 = str1.split(" ");
    const words2 = str2.split(" ");
    const intersection = words1.filter(word => words2.includes(word));
    const similarity = intersection.length / Math.max(words1.length, words2.length);
    return similarity;
  }
  
  function compareWithSimilarity(promptsArray, repliesArray, string) {
    let reply = null;
    let maxSimilarity = 0.65; // Minimum similarity threshold for an 80% match
  
    for (let x = 0; x < promptsArray.length; x++) {
      for (let y = 0; y < promptsArray[x].length; y++) {
        const similarity = stringSimilarity(promptsArray[x][y], string);
        if (similarity >= maxSimilarity) {
          reply = repliesArray[x][Math.floor(Math.random() * repliesArray[x].length)];
          break;
        }
      }
      if (reply) break;
    }
  
    return reply;
  }
  
  function addChat(input, product) {
    const messagesContainer = document.getElementById("messages");
  
    let userDiv = document.createElement("div");
    userDiv.id = "user";
    userDiv.className = "user response";
    userDiv.innerHTML = `<img src="user.png" class="avatar"><span>${input}</span>`;
    messagesContainer.appendChild(userDiv);
  
    let botDiv = document.createElement("div");
    let botImg = document.createElement("img");
    let botText = document.createElement("span");
    botDiv.id = "bot";
    botImg.src = "bot-mini.png";
    botImg.className = "avatar";
    botDiv.className = "bot response";
    botText.innerText = "Typing...";
    botDiv.appendChild(botText);
    botDiv.appendChild(botImg);
    messagesContainer.appendChild(botDiv);
    // Keep messages at most recent
    messagesContainer.scrollTop = messagesContainer.scrollHeight - messagesContainer.clientHeight;
  
    // Fake delay to seem "real"
    setTimeout(() => {
      botText.innerText = `${product}`;
      textToSpeech(product)
    }, 2000
    )
  
  }