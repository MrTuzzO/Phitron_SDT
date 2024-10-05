function monthlySavings(income, livingCost) {
    if (typeof livingCost != "number" & typeof income != "object") {
        return "invalid input";
    }

    let totalIncome = 0;
    for (let i = 0; i < income.length; i++) {
        if (income[i] >= 3000) {
            totalIncome += (income[i] - (income[i] * 0.2))
        } else totalIncome += income[i];
    }

    if (totalIncome >= livingCost) {
        return totalIncome - livingCost;
    } else return `"earn more"`

}

console.log(monthlySavings([1000, 2000, 3000], 5400));
console.log(monthlySavings([1000, 2000, 2500], 5000));
console.log(monthlySavings([900, 2700, 3400], 10000));
console.log(monthlySavings(100, [900, 2700, 34001]));