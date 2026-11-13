(() => {
  'use strict';

  const audio = document.getElementById('soundtrack');
  const audioToggle = document.getElementById('audioToggle');
  const audioCopy = document.getElementById('audioCopy');
  const openingButton = document.getElementById('openCurtain');
  const revealContent = document.getElementById('revealContent');
  const introContent = document.getElementById('introContent');
  const seeTicketButton = document.getElementById('seeTicket');
  const printButton = document.getElementById('printTicket');
  const sparkles = document.getElementById('sparkles');

  // Locally rendered, public-domain Beethoven excerpt; low volume for ambiance.
  audio.volume = 0.40;

  function setAudioVisual(playing) {
    audioToggle.setAttribute('aria-pressed', String(playing));
    audioToggle.setAttribute('aria-label', playing ? 'Metti in pausa la musica di Beethoven' : 'Attiva la musica di Beethoven');
    audioCopy.innerHTML = playing ? 'Musica <b>ON</b>' : 'Musica <b>OFF</b>';
  }

  async function startAudio() {
    try {
      await audio.play();
      setAudioVisual(true);
    } catch (error) {
      // Autoplay restrictions or unsupported file: a subsequent click can retry.
      setAudioVisual(false);
    }
  }

  audioToggle.addEventListener('click', () => {
    if (audio.paused) startAudio();
    else { audio.pause(); setAudioVisual(false); }
  });
  audio.addEventListener('pause', () => setAudioVisual(false));
  audio.addEventListener('play', () => setAudioVisual(true));
  audio.addEventListener('error', () => setAudioVisual(false));

  let opened = false;
  const positions = [
    [12,23],[22,38],[32,13],[43,30],[52,12],[65,23],[74,18],
    [81,44],[15,70],[28,85],[44,72],[58,83],[75,68],[90,76],
    [37,52],[61,54],[86,30],[9,52],[95,53]
  ];
  for (let i=0; i<positions.length; i++) {
    const star = document.createElement('i');
    star.className = 'spark';
    star.style.left = `${positions[i][0]}%`;
    star.style.top = `${positions[i][1]}%`;
    star.style.animationDelay = `${0.72+(i*0.17)%2.6}s`;
    sparkles.append(star);
  }

  openingButton.addEventListener('click', () => {
    if (opened) return;
    opened = true;
    startAudio();
    document.body.classList.add('is-open');
    document.getElementById('scrollHint').textContent = 'SCORRI PER CONTINUARE ↓';
    openingButton.disabled = true;
    introContent.setAttribute('aria-hidden', 'true');
    revealContent.removeAttribute('aria-hidden');
    window.setTimeout(() => seeTicketButton.focus({preventScroll:true}), 1250);
  });

  seeTicketButton.addEventListener('click', () => {
    document.getElementById('regalo').scrollIntoView({behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth'});
  });

  printButton.addEventListener('click', () => window.print());
})();
