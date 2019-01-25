function traverse(obj) {
  console.log(obj);
  if (obj.left) {
    traverse(obj.left);
  }
  if (obj.pitch) {
    console.log(obj.pitch);
  }
  if (obj.right) {
    traverse(obj.right);
  }
}

var melody2_mus =
{
  tag: 'seq',
  left:
  {
    tag: 'seq',
    left: { tag: 'note', pitch: 'a4', dur: 250 },
    right: { tag: 'note', pitch: 'b4', dur: 250 }
  },
  right:
  {
    tag: 'seq',
    left: { tag: 'note', pitch: 'c4', dur: 500 },
    right: { tag: 'note', pitch: 'd4', dur: 500 }
  }
}

traverse(melody2_mus);


