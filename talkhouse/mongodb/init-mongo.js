db = db.getSiblingDB('idk'); 

db.myCollection.insertMany([
    { name: "Item 1", description: "Description 1", quantity: 10 },
    { name: "Item 2", description: "Description 2", quantity: 20 },
    { name: "Item 3", description: "Description 3", quantity: 30 }
]);