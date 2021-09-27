const Discord = require('discord.js');
const simplydjs = require("simply-djs");

module.exports = {
    name: "calculator",
    usage: "`-calculator`",
    description: "Displays a virtual calculator.",
    run: async(client,message) => {
        simplydjs.calculator(message, {
            embedColor: "#00ff94",
            credit: false,
        })
    }   
}
