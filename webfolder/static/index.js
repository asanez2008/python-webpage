function deleteNote(blogId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ blogId: blogId }),
  }).then((_res) => {
    window.location.href = "/page2";
  });
}