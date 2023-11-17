class Singleton {
    private static instance: Singleton

    
    private constructor(public metaOne: string, public metaTwo: number){
    }

    public static getInstance(metaOne = '', metaTwo= 1): Singleton {
        if(!Singleton.instance)
            Singleton.instance = new Singleton(metaOne, metaTwo)
        return Singleton.instance
    }
}


// USAGE

const singleton = Singleton.getInstance()
const singleton2 = Singleton.getInstance()
const singleton3 = Singleton.getInstance()

console.log(singleton)
console.log(singleton === singleton2)
console.log(singleton === singleton3)