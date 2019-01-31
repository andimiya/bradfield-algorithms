var ways = [];

function checkIfValid(newArray) {
  // console.log(newArray);
  return false;
}

function findAllIps(IP) {
  var ipArray = [];
  ipArray = IP.split('')

  var dots = 0;
  var startingPoint = 0;

  while (startingPoint <= 5) {
    for (var i = startingPoint; i < ipArray.length; i++) {
      if (dots == 3) {
        return
      }
      else {
        var newArray = ipArray;
        ipArray.splice(i, 1, '.');
        checkIfValid(newArray);
      }
      console.log(newArray, 'array');
      dots++;
    }

    startingPoint++;
  }
}

findAllIps('521522')