function scale(el){
    el.classList.add('scale')
    el.classList.remove('unscale')
}


function unscale(el){
    el.classList.add('unscale')
    el.classList.remove('scale')
}


function highlight(el){
    el.classList.add('linksover')
}

function unhighlight(el){
    el.classList.remove('linksover')
}


function linkon(el){
    el.classList.add('linksover')
    el.classList.remove('links')
}


function linkoff(el){
    el.classList.add('links')
    el.classList.remove('linksover')
}


async function getspell(){

    var response = await fetch("https://www.dnd5eapi.co/api/spells");
    var spell_list = await response.json();

    random = Math.floor(Math.random() * 319)

    var spellurl = spell_list.results[random]['url'];


    var response = await fetch(`https://www.dnd5eapi.co${spellurl}`);
    var spell = await response.json();

    console.log(spell['name']);
    console.log(spell['desc'][0]);

    var dndspell = document.getElementById('dndspell');
    var dnddesc = document.getElementById('dnddesc');

    dndspell.innerText += spell['name'];
    dnddesc.innerText += spell['desc'][0];

    // var img = document.createElement("img")
    // img.src ="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/1200px-Image_created_with_a_mobile_phone.png";

    // dnd.appendChild(img)

    // console.log(img)
    // dnd.classList.push("white")





    // let el = document.getElementById("cat");
    // console.log(apiData)

    
    // console.log(random)

    // for (row in apiData)
    //     el.innerText += apiData[row]['text']
        


    return spell_list
}


async function getclass(){

    var response = await fetch("https://www.dnd5eapi.co/api/magic-items");

    var item_list = await response.json();

    random = Math.floor(Math.random() * 239)

    var itemurl = item_list.results[random]['url'];


    var response = await fetch(`https://www.dnd5eapi.co${itemurl}`);
    var item = await response.json();

    console.log(item['name'])
    for (row in item['desc'])
        console.log(item['desc'][row])


    var dnditem = document.getElementById('dnditem');
    var dnditemdesc = document.getElementById('dnditemdesc');

    dnditem.innerText += item['name'];
    for (row in item['desc'])
        dnditemdesc.innerText += item['desc'][row]






    return item_list

}
