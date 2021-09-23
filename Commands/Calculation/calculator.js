const Discord = require('discord.js');
const { Calculator } = require("weky");

module.exports = {
    name: "calculator",
    usage: "`-calculator`",
    description: "Displays a virtual calculator.",
    run: async(client,message) => {
        Calculator({
            message:message,
            embed: {
                title:"Virtual Calculator",
                color: "#00ff94",
                footer: "Calculator",
                timestamp: true,
            },
            disabledQuery: "true",
            invalidQuery: 'The provided equation is invalid!',
			othersMessage: 'Only <@{{author}}> can use the buttons!',
        })
    }   
}
