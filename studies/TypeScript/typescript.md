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
----
## Enums
```ts
enum Shoes{
    Nike,
    Vans,
    Diadora
}
let currentShoes = Shoes.Vans;
currentShoes = "Adidas" //Error
```
initializaztion
```ts
enum Priority{
    high = 1,
    medium,
    low
}
console.log(Priority.medium) //2
//fully init
enum HttpErrors{
    NotFound= 404,
    Success= 200,
    ServerError=500
}
```
can also contains strings
-------
## Aliases
```ts
type AlbumYear = number
type AlbumName = string
type AlbumFav = boolean
type Album = {
    year: AlbumYear,
    name: AlbumName,
    fav: AlbumFav
}
const varAlbumYear: AlbumYear = 2016
const varAlbumName: AlbumName = "Blonde"
const varAlbumFav: AlbumFav = true
const Album = {
    year: varAlbumYear,
    ..
}
```
-----
## Interface
Similar to [aliases](#Aliases) but applicated to [objects](#objects)
```ts
interface User{
    name: string,
    age: number
}
const myUser : User = {
    name: 'Alby',
    age: 23
}
//extending
interface superUser extends User{
    superpowers: boolean
}
```
----------
## Union types
when a can be more than a single type
```ts
function myF(value: string|number){
    console.log(value);
}
myF("Alby");
myF(23);
```

**Can throw error** when are used method of a specific type (*eg: toUpperCase and the value is a number*)

--------
## Functions
Functions can be declarated to return a spcific type.
```ts
function printDate(): string{
    console.log(moment().now());
}
```
### Parameters 
The normal ones are declared like variables are (var: type)<br>

#### Optionals and default
The same of objects:
```ts
function myF(optional?: any, default: number=10){
    //awsome code
}
```
#### Rest
Rest parameters are always arrays, so:
```ts
function add(a: number, b:number, ...rest: number[]){
    return a+b+rest.reduce((p,c)=>p+c,0);
}
```

#### Alias
```ts
type Negate= (value:number) => number;

const negateFunction: Negate = (value) => value*-1;
```
---------
## Casting

### as
```ts
let x: unknown = 'hey';
console.log((x as string).length); //3
let y: number=3
console.log((y as string).length); //undefined!

console.log((4 as string).length); //error!
```
We can also use '<>'
```ts
let x: unknown = 'hey';
console.log((<string>x).length);
```

### Force casting
To ovveride type errors -> first cast to 'unknown' then to the type
```ts
let x='hey';
console.log(((x as unknown) as number).lenght); //return undefined, 'hey' is not a number.. not error btw
```
--------
## Classes
```ts
class Album{
    name: string;
}
const mbtdf = new Album();
album.name='My beautiful twisted dark fantasy';
```
### Visibility
as usual.. 'public' is by default, 'protected' from class whose inherited, 'private' only from class itself.
```ts
class Album{
    private name: string;
    public costructor(nameP:string){
        this.name=nameP;
    }
    public getName():string{
        return name;
    }
}
var hnvm = new Album("Honestly, nevermind");
```
### Readonly
As the [readonly](#readonly) keyword, prevent variables to being changed.
```ts
class Album{
    private readonly year: number ;
    public constructor(yearP: number){
        this.year = yearP; //year can't be changed after first init
    }
}
```
### Inheritance
```ts
interface CoffeMachine{
    getCoffee: () => boolean;
}
class DeLonghi implements CoffeMachine {
    public constructor(protected readonly numModel: number, readonly name: string){

    }
    public getCoffee(): boolean{
        return function2MakeCoffeOn(numModel);
    }
}
```
### Extends
as seen before, there's the keyword 'extends'
```ts
class a{

}
class b extends a{
    //method of a inherited
}
```
### Override
Keyword 'override'
```ts
class a {
    function af(){
        console.log("yee");
    }
}
class b extends a{
    function override af():string{
        return "ye";
    }
}
```

### Abstract
keyword 'abstract'
```ts
abstract class Abs{
    public abstract absF(): number;
    public toString(): string{
        return "hey"
    }
}
class Realone extends Abs{
    public constructor(){
        super()
    }
    public absF():number{
        return 5;
    }
}
```
--------






















