function check_capiuas() {

   let numbers = db.phones.find({}, {_id: 0, display: 1}).toArray();

   let result = [];
   for (i in numbers) {
      let num = numbers[i]['display'].split('-')[1];
      result.push(num);
      for (let i2 = 0; i2 < num.length/2; i2++)
         if (num[i2] != num[num.length - i2 - 1]) {
            result.splice(result.indexOf(num), 1);
            break;
         }
   }

   return result;
}