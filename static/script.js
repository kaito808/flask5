// Let's assume this is your entire blog posts data from the database
var allPosts = [
  {
    name: "Story 1",
    category: "Emergent Readers: Levels A-C",
    content: "This is a story suitable for Emergent Readers",
  },
  {
    name: "Story 2",
    category: "Emergent Readers: Levels A-C",
    content: "This is another story suitable for Emergent Readers",
  },
  {
    name: "Story 3",
    category: "Early Readers: Levels D-I",
    content: "This is a story suitable for Early Readers",
  },
];

var postsInCategory = allPosts.filter(function (post) {
  return post.category === category;
});

for (var i = 0; i < postsInCategory.length; i++) {
  var post = postsInCategory[i];

  var postElement = document.createElement("div");
  postElement.className = "reading-level";

  var nameElement = document.createElement("h2");
  nameElement.textContent = post.name;
  postElement.appendChild(nameElement);

  var contentElement = document.createElement("p");
  contentElement.textContent = post.content;
  postElement.appendChild(contentElement);

  blogPostsContainer.appendChild(postElement);
}

//chatgpt
