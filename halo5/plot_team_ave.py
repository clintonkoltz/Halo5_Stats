import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

def plot_team_ave(X, Y, X_label, Y_label):

    team_colors = {
            'clg'      : 'blue',

            'e6'      : 'black',

            'nv'       : '#707b7c',

            'rng'  : 'red',

            'alg'      : 'orange',

            'eg'  : '#5F259F',

            'op'       : 'green',

            'tl'       : '#7fb3d5',
                }
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

    team_markers = {
            'clg'       : 'o',
            'alg'   : 'p',
            'e6'   : '*',
            'tl'   : 'D',
            'op' : '^',
            'eg' : 'h',
            'nv' : '+',
            'rng' : 'x',
                }

    Teams = {

        'clg' : [
                'CLG Royal 2',
                'CLG Frosty HCS',
                'CLG Snake Bite',
                'CLG LethuL HCS' ],
        'e6'  : [
                'E6 Huke HCS',
                'E6 Shooter',
                'E6 Cratos HCS',
                'E6 bubu dubu' ],
        'nv'  : [
                'nV Mikwen HCS',
                'nV eL ToWn',
                'nV RayneHCS',
                'nV Pistola HCS' ],
        'rng' : [
                'RNG Penguin HCS',
                'RNG Victory X',
                'RNG Ninja HCS',
                'RNG Commonly' ],
        'alg' : [
                'ALG RyaNoob',
                'ALG Heinz HCS',
                'ALGPredevonator',
                'ALG ContrA HCS'],
        'eg'  : [
                'EG SuspectorHCS',
                'EG Snip3downHCS',
                'EG Lunchbox HCS',
                'EG Roy HCS' ],
        'op'  : [
                'OG ACE HCS',
                'OG Str8 SickHCS',
                'OG Maniac HCS',
                'OG APG HCS' ],
        'tl'  : [
                'TL Eco HCS',
                'TL StelluR',
                'TL Spartan HCS',
                'TL Danoxide' ]
        }


    x_ave ={}
    y_ave = {}

    for i in Teams:
        x_ave[i] = (X[Teams[i][0]] + X[Teams[i][1]] + X[Teams[i][2]] +
                X[Teams[i][3]] ) / 4.0
        y_ave[i] = (Y[Teams[i][0]] + Y[Teams[i][1]] + Y[Teams[i][2]] +
                Y[Teams[i][3]] )  / 4.0
    fig = plt.figure()
    fig.subplots_adjust(left=0.05, right=0.86)
    ax1 = fig.add_subplot(111)
#    ax1.plot([100,500],[100,500])
    ax1.set_xlabel(X_label, fontsize=14)
    ax1.set_ylabel(Y_label, fontsize=14)
    ax1.grid()
    for i in team_colors.keys():
        ax1.scatter(x_ave[i], y_ave[i], label=i,
                color=team_cb_colors[i],marker=team_markers[i],s=80)
    fontP = FontProperties()
    fontP.set_size(15)
    hand, labels = ax1.get_legend_handles_labels()
    hand = np.array(hand)
    labels = np.array(labels)
    ind = labels.argsort()
    leg = ax1.legend(hand[ind], labels[ind], prop=fontP)
    leg.draggable()
    fig.show()



