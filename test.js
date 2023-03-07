var { OmniverseJS, OmniFolderEntry, OmniFolderEntryPtr } = require("./ovWrapper.js")

var ov = new OmniverseJS();

ov.initialize();

console.log(ov.getVersion());
console.log("Username is: " + ov.getUsername("omniverse://localhost/"));
console.log("Shutting down");
ov.shutdown();