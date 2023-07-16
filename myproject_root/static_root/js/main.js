function getPostList(){
    fetch('/api/myproject/')
    .then(res => res.json())
    .then(data => {
        console.log(data);
    })
    .catch(err => {
        console.error(err);
    })
 }
 
 
 getPostList()