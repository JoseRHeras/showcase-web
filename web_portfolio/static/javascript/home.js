document.addEventListener("DOMContentLoaded", () =>{
    const toolbarItems = document.querySelectorAll('.toolbar_item')
    
    
    toolbarItems.forEach(element => {
        element.addEventListener('click', () => {
            
            toolbarItems.forEach(element => {
                element.classList.remove('active')
            })

            element.classList.add('active')
        })
    })


    // Add animation objects
    const animationItemsList = document.getElementById('animation_items_list')

    let itemCount = 5

    for(let n = 0; n < itemCount; n++) {
        const li = document.createElement('li')
        li.classList.add('animation_item')
        animationItemsList.appendChild(li)
    }
})