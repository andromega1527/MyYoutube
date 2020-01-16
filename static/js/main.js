var button = document.querySelector('button.link-left-bar')

button.onclick = function() {
    var left_bar = document.querySelector('div.left-bar')

    left_bar.getAttribute('hidden') != null ? left_bar.removeAttribute('hidden') : left_bar.setAttribute('hidden', 'hidden')
}