const figlet = require("figlet")

module.exports = {
    name: "ascii",
    usage: "-ascii <text>",
    description: "Sends the text as ascii art.",
    run: async(client,message,args) => {
        if (!args[0]) return message.reply("You must input some text to use this command...");
        figlet(args.slice(0).join("```\n  \n```"), function (err, data) {
            if (err) {
                console.log('Something went wrong...');
                console.dir(err);
                return;
            }
            message.channel.send("```\n"+data+"\n```", {
                code: "AsciiDoc"
            }).catch(() => message.reply("The given text is too long, try again..."))
        });
    }
}