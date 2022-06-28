import { Observable } from 'rxjs';

const numberStream = new Observable((subscriber) => {
  for (let i = 0; i < 10; i++) {
    subscriber.next(i);
  }

  throw new Error('123');

  subscriber.complete();
});

// Subscriber 1: immediate
let subscriber1 = [];
numberStream.subscribe(
  (val) => {
    console.log('val pushed:', val);
    subscriber1.push(val);
  },
  (err) => console.error(err),
  () => console.log('subscriber1 complete:', subscriber1),
);
console.log('L21', subscriber1);

console.log('subscriber 2:');
// Subscriber 2: after 2 seconds
setTimeout(() => {
  let subscriber2 = [];
  numberStream.subscribe(
    (val) => {
      console.log('val pushed:', val);
      subscriber2.push(val);
    },
    (err) => console.error(err),
    () => console.log('subscriber2 complete:', subscriber2),
  );
  console.log('L35', subscriber2);
}, 2000);

