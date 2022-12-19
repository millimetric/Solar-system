import matplotlib.pyplot as plt
import numpy as np
import astronomical_bodies
import solar_masses

plt_dict = {'title': 'Astronomical bodies, solar system',
            'ax1_ylabel': '4 inner',
            'ax2_ylabel': '4 most massive',
            'ax3_ylabel': '8 planets of the solar system',
            'ax4_ylabel': 'Mass, planets vs sun [%]'
            }
# 'x1': astronomical_bodies.mass[0:3]'

# DATA
x1 = np.array(solar_masses.masses[0:4])
y1 = np.array(solar_masses.names[0:4])
x2 = np.array(solar_masses.masses[4:8])
y2 = np.array(solar_masses.names[4:8])
x3 = np.array(solar_masses.masses[0:8])
y3 = np.array(solar_masses.names[0:8])
x4 = np.array([solar_masses.percentage_mass[0],solar_masses.percentage_mass[1]])
y4 = np.array(['Planets','Sun'])

# FIGURE 
mm = 1/25.4
fig, (ax1,ax2,ax3) = plt.subplots(3,1,figsize=(150*mm,250*mm))
fig.suptitle(plt_dict['title'], va= 'top', ha='right', fontdict={'family':'consolas','color':'k','size':10,'weight':'bold'})

# PLOT1
ax1.barh(y1, x1, align='center', height=0.25, color=['#B5AA9A','#b06f2d','#64B9DB','#F5825B'])
ax1.set_xscale('log', base=10)
ax1.set_xlim(1e22,1e25)
ax1.set_ylabel(plt_dict['ax1_ylabel'], fontdict={'family':'consolas','color':'k','size':9,'weight':'bold'})
ax1.yaxis.labelpad = 20
ax1.spines[["top", "right"]].set_visible(False)
ax1.tick_params(which='major', width=2.0, length=10, labelsize=8)

# PLOT2
ax2.barh(y2, x2, align='center', height=0.25, color=['#CFBCA2', '#A29F84', '#C3E9EC', '#4B526D'])
ax2.set_xscale('log', base=10)
ax2.set_xlim(1e24,1e28)
ax2.set_ylabel(plt_dict['ax2_ylabel'], fontdict={'family':'consolas','color':'k','size':9,'weight':'bold'})
ax2.yaxis.labelpad = 20
ax2.spines[["top", "right"]].set_visible(False)
ax2.tick_params(which='major', width=2.0, length=10, labelsize=8)

# PLOT3
ax3.barh(y3, x3, align='center', height=0.5)
b3_label = ax3.barh(y3, x3, align='center', height=0.5,color=['#B5AA9A','#B06F2D','#64B9DB', '#F5825B','#CFBCA2','#A29F84','#C3E9EC','#4B526D'])
ax3.bar_label(b3_label, labels=[solar_masses.masses[0]], padding=3)
ax3.set_xscale('log', base=10)
ax3.set_xlim(1e23,1e28)
ax3.set_xlabel('Mass [kg]', fontdict={'family':'consolas','color':'k','size':9,'weight':'bold'})
ax3.set_ylabel(plt_dict['ax3_ylabel'], fontdict={'family':'consolas','color':'k','size':9,'weight':'bold'})
ax3.yaxis.labelpad = 20
ax3.spines[["top", "right"]].set_visible(False)
ax3.tick_params(which='major', width=2.0, length=10, labelsize=8)

# PLOT4
# ax4.barh(y4, x4, align='center', height=0.05, color=['k','y'])
# b4_label = ax4.barh(y4, x4, align='center', height=0.025, color=['k','y'])
# ax4.bar_label(b4_label, labels=[round(solar_masses.percentage_mass[0],2),round(solar_masses.percentage_mass[1],2)], padding=3)
# ax4.set_xscale('log', base=10)
# ax4.set_xlabel('Mass [kg]', fontdict={'family':'consolas','color':'k','size':9,'weight':'bold'})
# #ax4.xaxis.labelpad = 20
# ax4.set_ylabel(plt_dict['ax4_ylabel'], fontdict={'family':'consolas','color':'k','size':9,'weight':'bold'})
# ax4.yaxis.labelpad = 25
# ax4.spines[["top", "right"]].set_visible(False)
# ax4.tick_params(which='major', width=2.0, length=10, labelsize=8)
#
#
plt.show()


