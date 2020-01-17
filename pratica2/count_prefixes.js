function count_prefixes() {

   var prefixes = db.phones.distinct('components.prefix');

   var result = {};
   for(i in prefixes) {
      result[prefixes[i]] = db.phones.find({
         'components.prefix': prefixes[i]
      }).count()
   }

   return result;
}