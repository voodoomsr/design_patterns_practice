import {Singleton} from '../src/singleton'; // replace with actual path to your singleton class

describe('Singleton Class Test', () => {
    it('creates only one instance', () => {
        const instance1 = Singleton.getInstance();
        const instance2 = Singleton.getInstance();

        expect(instance1).toBe(instance2);
    });
});