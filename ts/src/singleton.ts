export class Singleton {
    private static instance: Singleton

    
    private constructor(public metaOne: string, public metaTwo: number){
    }

    public static getInstance(metaOne = '', metaTwo= 1): Singleton {
        if(!Singleton.instance)
            Singleton.instance = new Singleton(metaOne, metaTwo)
        return Singleton.instance
    }
}
