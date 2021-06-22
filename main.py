import os
from pynput import keyboard

from observer import SessionManager

welcome = """
   ,--,
,---.'|
|   | :                                      ,---,              ___
:   : |                                   ,`--.' |            ,--.'|_
|   ' :                    ,----,         |   :  :     ,---,  |  | :,'           __  ,-.
;   ; '                  .'   .`|         :   |  ' ,-+-. /  | :  : ' :         ,' ,'/ /|
'   | |__  ,--.--.    .'   .'  .'     .--,|   :  |,--.'|'   .;__,'  /    ,---. '  | |' |
|   | :.'|/       \ ,---, '   ./    /_ ./|'   '  |   |  ,"' |  |   |    /     \|  |   ,'
'   :    .--.  .-. |;   | .'  /  , ' , ' :|   |  |   | /  | :__,'| :   /    /  '  :  /
|   |  ./ \__\/: . .`---' /  ;--/___/ \: |'   :  |   | |  | | '  : |__.    ' / |  | '
;   : ;   ," .--.; |  /  /  / .`|.  \  ' ||   |  |   | |  |/  |  | '.''   ;   /;  : |
|   ,/   /  /  ,.  |./__;     .'  \  ;   :'   :  |   | |--'   ;  :    '   |  / |  , ;
'---'   ;  :   .'   ;   |  .'      \  \  ;;   |.'|   |/       |  ,   /|   :    |---'
        |  ,     .-.`---'           :  \  '---'  '---'         ---`-'  \   \  /
         `--`---'                    \  ' ;                             `----'
                                      `--`
Logging outages is simple
"""

print(welcome, flush=True)


def notify(message, icon_name="printer-remote"):
    os.system(f"notify-send -i {icon_name} -t 10000 '{message}'")


def on_start():
    manager = SessionManager.instance()
    session = manager.current_session()

    if session is None:
        manager.start_session()
        notify('Sessão começou agora!')
    else:
        notify('Você ainda não encerrou a sua sessão enterior.')


def on_finish():
    manager = SessionManager.instance()

    if manager.current_session():
        manager.finish_session()
        session = manager.current_session()

        notify(
            f"A sessão durou {str(session.resume())} minutos e será registrada como: {session.reason()}")
    else:
        notify('Nenhuma sessão iniciada.')


def on_meeting():
    manager = SessionManager.instance()
    if manager.current_session():
        manager.add_reason_on_current_session("Reunião")
        notify("Será registrada como: Reunião")


def on_investigation():
    manager = SessionManager.instance()
    if manager.current_session():
        manager.add_reason_on_current_session("Investigação de Bug")
        notify("Será registrada como: Investigação de Bug")


def on_flow():
    manager = SessionManager.instance()
    if manager.current_session():
        manager.add_reason_on_current_session(
            "No meio de um fluxo de programação")
        notify("Será registrada como: No meio de um fluxo de programação")


with keyboard.GlobalHotKeys({
        '<ctrl>+<alt>+s': on_start,
        '<ctrl>+<alt>+f': on_finish,
        '<ctrl>+<alt>+m': on_meeting,
        '<ctrl>+<alt>+i': on_investigation,
        '<ctrl>+<alt>+p': on_flow,
}) as h:
    h.join()
