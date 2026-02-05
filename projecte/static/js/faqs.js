/**
 * Mostra o amaga la resposta a una pregunta freqüent
 * @param {HTMLElement} button - El botó de la pregunta
 */
function mostraResposta(button) {
    const itemPreguntes = button.parentElement;
    const resposta = itemPreguntes.querySelector('.faq-answer');
    const icona = button.querySelector('.faq-icon');

    itemPreguntes.classList.toggle('actiu');

    if (itemPreguntes.classList.contains('actiu')) {
        icona.textContent = '−';
        resposta.style.maxHeight = resposta.scrollHeight + 'px';
    } else {
        icona.textContent = '+';
        resposta.style.maxHeight = '0';
    }
}
