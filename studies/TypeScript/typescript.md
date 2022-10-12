# TypeScript

JavaScript with data type.

Created by Microsoft 🤮, but the language is cool to use!

- Can be converted into JavaScript so it can be runned everywhere JavaScript can be run.
> anyway has a compiler: `$ npm -i typescript; npx tsc` -> print the verison

--------------------
##  Type

### Simple ones

- boolean
- number
- string

#### Assignment

1. Explicit
```ts
let x: string = "Alby";
x= 33; //throw an error
```

2. Implicit (ts will guess the typo, like js does):
```ts
let x = "Alby";
x= 33; //No eerror thrown
```

### Special ones

#### Any
Allows all the type to be used.
```ts
let x = true;
x = "51"; //error, type string is not assignable to type boolean
Math.round(x) //error

//with any no error->
let x: any = true; 
```

#### Unknown
Similar to [any](####any), but safer.

You should use it when you don't know the type, and you'd like to cast later. <br>
*Casting using keyword "as"*

#### Never
Throw an error when it is defined.
Dunno man

#### Undefined/null
Like javascript


-----------
## Array

```ts
const arr: string[] = [];
arr.push("Alby");
```
**readonly**: keyword which prevent arrays to be changed.
```ts
const arr: readonly string[] = [];
arr.push("Alby"); //error
```
### Inferred
ts will gues
```ts
const arr = [1,2,3];
arr.push(5); //OK
arr.push("7"); //error
let head: number = arr[0]; //OK
```
---------------------
## Tuples

Allows multi type of data into a set.
```ts
let myTuple = [number, boolean, string]
myTuple=[5,true,"Albyy"];
```
**readonly class**
-> allows us to define a tuple and assign it once some values whose can be changed.

### Named tuples

```ts
const user: [name: string, age: number] = ["alby",23];
//destructuring
const [n,a]= user;
```

-----
## Objects
```ts
const album: { 
    name: string,
    artist: string,
    year: number
}= {"Nectar","Joji",2019};
album.name='Ballads 1' //ok
album.name=2018 //error
```
### Optional props
```ts
const album: { 
    name: string,
    artist: string,
    year: number
}= {"Nectar","Joji"}; //ERROR-> missing year

const album2:{
    name: string,
    artist: string,
    year? : number
}= {"Views","Drake"}; //OK
album2.year=2016; //OK
```
