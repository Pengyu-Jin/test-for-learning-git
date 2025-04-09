class Person {
    constructor(firstName, lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    getName() {
        const name = this.firstName +'' + this.lastName;
        return name;
    }

    say() {
        const name = this.getName();
        const text = name + ":" + this.age;
    }
}

const person = new Person('John', 'Doe');
const text = person.say();
console.log(text);