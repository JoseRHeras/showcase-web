document.addEventListener("DOMContentLoaded", () =>{
    
    // Add animation objects
    const animationBox = document.createElement('div')
    const animationItems = document.createElement('ul')

    animationBox.classList.add('animation_box')
    animationItems.setAttribute('id','animation_items_list')

    for (let index = 0; index < 5; index++) {
        const li = document.createElement('li')
        li.classList.add('animation_item')
        animationItems.appendChild(li)     
    }

    animationBox.appendChild(animationItems)
    document.getElementsByClassName('wrapper')[0].appendChild(animationBox)   
})