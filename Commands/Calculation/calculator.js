const simplydjs = require("simply-djs")

module.exports = {
    name: "calculator",
    usage: "`-calculator`",
    description: "Displays a virtual calculator.",
    run: async(message) => {
        simplydjs.calculator(message,{
            embedColor: "#00ff94",
        })
    }   
}