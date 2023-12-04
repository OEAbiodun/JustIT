const quotes=[
    {
        quote:` Arise, shine; for thy light is come, and the glory of the LORD is risen upon thee.`,
        verse:`- Isaiah 60:1`
    },
    {
        quote:` For, behold, the darkness shall cover the earth, and gross darkness the people: but the LORD shall arise upon thee, and his glory shall be seen upon thee.`,
        verse:`- Isaiah 60:2`
    },
    {
        quote:` Be careful, however, that the exercise of your rights does not become a stumbling block to the weak.`,
        verse:`- 1 Corinthians 8:9`
    },
    {
        quote:`There is a time for everything, and a season for every activity under the heavens.`,
        verse:`- Ecclesiastes 3:1`
    },
    {
        quote:`Therefore each of you must put off falsehood and speak truthfully to your neighbor, for we are all members of one body.`,
        verse:`- Ephesians 4:25 `
    },
    {
        quote:` But the fruit of the Spirit is love, joy, peace, patience, kindness, goodness, faithfulness.`,
        verse:`- Galatians 5:22`
    },
    {
        quote:`Now faith is being sure of what we hope for and certain of what we do not see.`,
        verse:`- Hebrews 11:1`
    },
    {
        quote:`Keep on loving one another as brothers and sisters.`,
        verse:`- Hebrews 13:1`
    },
    {
        quote:`Woe to those who call evil good and good evil, who put darkness for light and light for darkness, who put bitter for sweet and sweet for bitter.`,
        verse:`- Isaiah 5:20`
    },
    {
        quote:`Consider it pure joy, my brothers and sisters, whenever you face trials of many kinds.`,
        verse:`- James 1:2`
    },
    {
        quote:`The heart is deceitful above all things and beyond cure. Who can understand it?`,
        verse:`- Jeremiah 17:9`
    },
    {
        quote:`The light shines in the darkness, and the darkness has not overcome it.`,
        verse:`- John 1:5`
    },
    {
        quote:`There is no fear in love. But perfect love drives out fear, because fear has to do with punishment. The one who fears is not made perfect in love.`,
        verse:`- 1 John 4:18`
    },
    {
        quote:`Do to others as you would have them do to you.`,
        verse:`- Luke 6:31`
    },
    {
        quote:`Blessed are the meek, for they will inherit the earth.`,
        verse:`- Matthew 5:5`
    },
]
const toggleBtn = document.querySelector('.btn');
toggleBtn.addEventListener('click', () => {
document.documentElement.classList.toggle('dark-mode');
});


const moreQuote = document.getElementById('morequote');
const quote = document.querySelector('.quote');
const book = document.querySelector('.verse');
const soundbtn = document.querySelector('.sound');
const copybtn = document.querySelector('.copy');




moreQuote.addEventListener('click',()=>{
    let random = Math.floor(Math.random()*quotes.length);
    quote.innerText=quotes[random].quote;
    book.innerText=quotes[random].verse;
})

soundbtn.addEventListener("click", ()=>{
    let utterance = new SpeechSynthesisUtterance(`${quote.innerText} book of ${book.innerText}`);
    speechSynthesis.speak(utterance);
})

copybtn.addEventListener("click", ()=>{
    navigator.clipboard.writeText(quote.innerText + book.innerText);
})