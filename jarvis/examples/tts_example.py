import torch
from TTS.api import TTS
from pydub.playback import play
from pydub import AudioSegment

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)
print("\n".join(TTS().list_models().list_models()))

# Init TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

# Run TTS
# ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
# Text to speech list of amplitude values as output
wav = tts.tts_to_file(
    text="""
    Un caldo pomeriggio d'estate, il gatto Fufolo era steso al sole sulla terrazza, godendosi la calda luce e le dolci zefire. Improvvisamente, sentì un movimento sottostante e si accigliò, i suoi occhi verdi concentrati sulla minima perturbazione del panorama.

Ecco che il topo Tomasso, un'intrepida creatura con la pelliccia grigia e gli occhietti brillanti, era emerso dalla fessura della muratura. Fufolo non perse tempo: si alzò in punta di piedi, le sue zampe anteriori tese come frecce, pronte a colpire il nemico.

Tommaso, però, non aveva intenzione di arrendersi. Si fece avanti, la coda ondeggiante come una bandiera, e si mise a scappellare velocemente attorno alla terrazza, sfidando Fufolo a inseguirlo.    

Il gatto, con un'agilità incredibile, si lanciò all'inseguimento del topo, i suoi artigli sulla pietra. La corsa fu breve ma intensa, finché Tomasso non si nascose in un buco della parete e Fufolo non dovette ammettere la sconfitta.

E così, il gatto e il topo si separarono, ognuno ritornando al proprio territorio, pronti a ricominciare la loro eterna lotta. Ma nello stesso tempo, erano entrambi consapevoli che la loro amicizia nascosta era più forte di ogni conflitto.
    """,
    speaker_wav="tmp/output.wav",
    language="it",
    file_path="tmp/tts.wav",
)
song = AudioSegment.from_wav("tmp/tts.wav")
play(song)
