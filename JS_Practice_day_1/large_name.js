var friends = ["rahim", "karim", "abdul", "sadsd", "heroAlom"];
var largeName = "";
for (let i = 0; i < friends.length; i++) {
    if (friends[i].length > largeName.length) largeName = friends[i];
}
console.log(largeName); //heroAlom