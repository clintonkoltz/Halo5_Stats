import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

def plot_data(X, Y, X_label, Y_label):

    team_cb_colors = {
            'clg'      : (.0,.45,.70),

            'e6'      : 'black',

            'nv'       : (.80,.60,.70),

            'rng'  : (.80,.40,0),

            'alg'      : (.90,.60,0),

            'eg'  : (.95,.90,.25),

            'op'       : (0,.60,.50),

            'tl'       : (.35,.70,.90),
                }

    player_cb_colors = {
            'CLG Royal 2'      : (.0,.45,.70),
            'CLG Frosty HCS'   : (.0,.45,.70),
            'CLG Snake Bite'   : (.0,.45,.70),
            'CLG LethuL HCS'   : (.0,.45,.70),

            'E6 Huke HCS'      : 'black',
            'E6 Shooter'       : 'black',
            'E6 Cratos HCS'    : 'black',
            'E6 bubu dubu'     : 'black',

            'nV Mikwen HCS'    : (.80,.60,.70),
            'nV eL ToWn'       : (.80,.60,.70),
            'nV RayneHCS'      : (.80,.60,.70),
            'nV Pistola HCS'   : (.80,.60,.70),

            'RNG Penguin HCS'  : (.80,.40,0),
            'RNG Victory X'    : (.80,.40,0),
            'RNG Ninja HCS'    : (.80,.40,0),
            'RNG Commonly'     : (.80,.40,0),

            'ALG RyaNoob'      : (.90,.60,0),
            'ALG Heinz HCS'    : (.90,.60,0),
            'ALGPredevonator'  : (.90,.60,0),
            'ALG ContrA HCS'   : (.90,.60,0),

            'EG SuspectorHCS'  : (.95,.90,.25),
            'EG Snip3downHCS'  : (.95,.90,.25),
            'EG Lunchbox HCS'  : (.95,.90,.25),
            'EG Roy HCS'       : (.95,.90,.25),

            'OG ACE HCS'       : (0,.60,.50),
            'OG Str8 SickHCS'  : (0,.60,.50),
            'OG Maniac HCS'    : (0,.60,.50),
            'OG APG HCS'       : (0,.60,.50),

            'TL Eco HCS'       : (.35,.70,.90),
            'TL StelluR'       : (.35,.70,.90),
            'TL Spartan HCS'   : (.35,.70,.90),
            'TL Danoxide'      : (.35,.70,.90),

                }

    player_colors = {
            'CLG Royal 2'      : 'blue',
            'CLG Frosty HCS'   : 'blue',
            'CLG Snake Bite'   : 'blue',
            'CLG LethuL HCS'   : 'blue',

            'E6 Huke HCS'      : 'black',
            'E6 Shooter'       : 'black',
            'E6 Cratos HCS'    : 'black',
            'E6 bubu dubu'     : 'black',

            'nV Mikwen HCS'    : '#707b7c',
            'nV eL ToWn'       : '#707b7c',
            'nV RayneHCS'      : '#707b7c',
            'nV Pistola HCS'   : '#707b7c',

            'RNG Penguin HCS'  : 'red',
            'RNG Victory X'    : 'red',
            'RNG Ninja HCS'    : 'red',
            'RNG Commonly'     : 'red',

            'ALG RyaNoob'      : 'orange',
            'ALG Heinz HCS'    : 'orange',
            'ALGPredevonator'  : 'orange',
            'ALG ContrA HCS'   : 'orange',

            'EG SuspectorHCS'  : '#5F259F',
            'EG Snip3downHCS'  : '#5F259F',
            'EG Lunchbox HCS'  : '#5F259F',
            'EG Roy HCS'       : '#5F259F',

            'OG ACE HCS'       : 'green',
            'OG Str8 SickHCS'  : 'green',
            'OG Maniac HCS'    : 'green',
            'OG APG HCS'       : 'green',

            'TL Eco HCS'       : '#7fb3d5',
            'TL StelluR'       : '#7fb3d5',
            'TL Spartan HCS'   : '#7fb3d5',
            'TL Danoxide'      : '#7fb3d5',

            'Rammyy'           : 'magenta'
                }

    player_markers = {
            'CLG Royal 2'      : 'o',
            'CLG Frosty HCS'   : '^',
            'CLG Snake Bite'   : '*',
            'CLG LethuL HCS'   : 'D',

            'E6 Huke HCS'      : 'o',
            'E6 Shooter'       : '^',
            'E6 Cratos HCS'    : '*',
            'E6 bubu dubu'     : 'D',

            'nV Mikwen HCS'    : 'o',
            'nV eL ToWn'       : '^',
            'nV RayneHCS'      : '*',
            'nV Pistola HCS'   : 'D',

            'RNG Penguin HCS'  : 'o',
            'RNG Victory X'    : '^',
            'RNG Ninja HCS'    : '*',
            'RNG Commonly'     : 'D',

            'ALG RyaNoob'      : 'o',
            'ALG Heinz HCS'    : '^',
            'ALGPredevonator'  : '*',
            'ALG ContrA HCS'   : 'D',

            'EG SuspectorHCS'  : 'o',
            'EG Snip3downHCS'  : '^',
            'EG Lunchbox HCS'  : '*',
            'EG Roy HCS'       : 'D',

            'OG ACE HCS'       : 'o',
            'OG Str8 SickHCS'  : '^',
            'OG Maniac HCS'    : '*',
            'OG APG HCS'       : 'D',

            'TL Eco HCS'       : 'o',
            'TL StelluR'       : '^',
            'TL Spartan HCS'   : '*',
            'TL Danoxide'      : 'D'
                }


    fig = plt.figure()
    fig.subplots_adjust(left=0.05, right=0.86)
    ax1 = fig.add_subplot(111)
#    ax1.plot([100,500],[100,500])
    ax1.set_xlabel(X_label, fontsize=14)
    ax1.set_ylabel(Y_label, fontsize=14)
    ax1.grid()
    for i in player_markers.keys():
        ax1.scatter(X[i], Y[i], label=i, color=player_cb_colors[i],
                marker=player_markers[i],s=80)
    fontP = FontProperties()
    fontP.set_size(15)
    hand, labels = ax1.get_legend_handles_labels()
    hand = np.array(hand)
    labels = np.array(labels)
    ind = labels.argsort()
    leg = ax1.legend(hand[ind], labels[ind], prop=fontP)
    leg.draggable()
    fig.show()



