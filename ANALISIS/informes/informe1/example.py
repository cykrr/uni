import random
from termcolor import colored
import copy

def sort(a: list, verbose: bool = False):
    n = len(a)
    if verbose: print("Arreglo", a, ":")
    for i in range(1, n):
        if verbose: print(a)
        for j in range(0, i):
            if a[i] < a[j]:
                if verbose:
                    print(a)
                    print ("swap: (", a[i], ",", a[j], ")")
                a[i], a[j] = a[j], a[i]
    return a

def bub_sort(a: list[int], verbose: bool = False):
    n = len(a);
    swapped = False;
    for i in range(n-1):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                swapped = True
                a[j], a[j + 1] = a[j + 1], a[j]
        if not swapped:
            return a
    return a

def ins_sort(a: list[int], verbose: bool = False):
    n = len(a)
    if verbose: print("Arreglo", a, ":")
    for i in range(1, n):
        if verbose: print(a)
        for j in range(i, 2, -1):
            if a[j] < a[j-1]:
                if verbose: 
                    print(a)
                    print ("swap: (", a[i], ",", a[j], ")")
                a[j], a[j-1] = a[j-1], a[j]
            else: 
                break
    return a

a = [831, 367, 101, 365, 37, 763, 355, 688, 866, 63, 944, 448, 142, 48, 598, 957, 269, 205, 762, 393, 755, 580, 786, 714, 546, 124, 164, 509, 121, 909, 210, 760, 68, 593, 694, 709, 421, 410, 889, 104, 610, 863, 316, 473, 661, 157, 810, 984, 201, 283, 816, 454, 682, 336, 742, 110, 247, 141, 33, 220, 71, 878, 974, 923, 549, 527, 178, 408, 179, 679, 99, 288, 458, 782, 109, 189, 667, 927, 592, 857, 797, 443, 89, 776, 406, 513, 240, 361, 453, 730, 173, 521, 558, 700, 870, 230, 853, 664, 617, 186, 391, 449, 618, 897, 613, 686, 403, 531, 177, 740, 381, 905, 146, 517, 298, 135, 221, 575, 471, 291, 168, 625, 295, 505, 813, 250, 653, 851, 188, 934, 570, 64, 586, 105, 539, 167, 469, 131, 519, 997, 924, 568, 806, 457, 281, 844, 952, 744, 193, 993, 518, 725, 265, 442, 368, 875, 27, 123, 34, 893, 163, 307, 418, 780, 654, 835, 452, 502, 601, 249, 305, 441, 712, 789, 753, 496, 262, 120, 525, 607, 425, 556, 978, 294, 450, 324, 435, 956, 768, 685, 508, 325, 231, 461, 659, 258, 604, 76, 788, 584, 678, 903, 192, 176, 304, 504, 117, 35, 596, 485, 238, 311, 916, 969, 572, 255, 936, 528, 122, 232, 15, 506, 116, 975, 647, 216, 468, 470, 310, 347, 540, 327, 805, 149, 191, 820, 649, 669, 481, 75, 264, 621, 630, 594, 769, 382, 965, 390, 706, 901, 181, 612, 8, 728, 404, 935, 354, 913, 445, 812, 946, 398, 876, 172, 170, 995, 65, 748, 342, 754, 732, 614, 854, 578, 129, 85, 293, 493, 665, 349, 243, 705, 215, 1000, 826, 976, 18, 512, 747, 40, 872, 200, 386, 739, 494, 530, 821, 992, 50, 781, 278, 4, 88, 326, 440, 451, 62, 793, 727, 919, 733, 980, 792, 446, 275, 416, 930, 171, 918, 384, 750, 571, 879, 371, 379, 31, 554, 632, 162, 868, 849, 638, 289, 684, 44, 814, 565, 940, 939, 95, 409, 154, 828, 547, 971, 892, 438, 566, 966, 953, 290, 348, 962, 689, 840, 148, 910, 785, 702, 658, 692, 666, 152, 595, 277, 235, 884, 874, 981, 284, 634, 676, 973, 600, 888, 322, 161, 655, 328, 691, 958, 950, 850, 532, 486, 949, 941, 353, 717, 66, 587, 603, 510, 697, 147, 845, 233, 856, 861, 894, 529, 931, 229, 67, 244, 751, 933, 599, 369, 723, 864, 880, 415, 915, 3, 209, 809, 2, 434, 865, 38, 869, 339, 23, 370, 650, 802, 859, 203, 463, 873, 611, 921, 140, 631, 13, 619, 538, 690, 424, 52, 749, 729, 480, 591, 431, 366, 286, 990, 787, 836, 668, 343, 801, 204, 55, 10, 46, 19, 127, 583, 766, 551, 811, 256, 752, 886, 945, 227, 119, 300, 32, 881, 680, 5, 620, 642, 360, 22, 707, 57, 226, 1, 555, 818, 775, 125, 622, 560, 731, 608, 972, 194, 345, 321, 756, 466, 796, 320, 718, 190, 847, 791, 102, 573, 535, 626, 335, 675, 357, 158, 334, 333, 557, 214, 597, 589, 495, 72, 569, 929, 394, 358, 211, 439, 895, 395, 126, 90, 217, 479, 911, 695, 784, 841, 559, 832, 602, 42, 515, 69, 770, 902, 363, 488, 299, 380, 577, 208, 652, 254, 83, 660, 891, 185, 899, 84, 39, 737, 153, 151, 182, 514, 341, 60, 329, 80, 338, 412, 136, 627, 757, 59, 401, 704, 803, 641, 252, 423, 846, 270, 12, 261, 285, 359, 212, 492, 274, 150, 734, 670, 107, 114, 960, 955, 500, 383, 467, 741, 133, 885, 351, 942, 542, 112, 437, 429, 436, 947, 306, 807, 180, 696, 323, 920, 155, 644, 187, 132, 499, 968, 639, 239, 207, 838, 11, 79, 24, 459, 699, 234, 907, 392, 49, 779, 716, 308, 77, 465, 848, 407, 928, 548, 21, 948, 579, 82, 671, 951, 388, 629, 58, 646, 483, 883, 236, 550, 890, 507, 344, 91, 246, 111, 839, 722, 169, 96, 225, 989, 456, 490, 681, 396, 656, 544, 350, 302, 954, 988, 268, 251, 70, 199, 651, 636, 822, 53, 197, 698, 9, 7, 906, 272, 932, 373, 43, 877, 758, 17, 609, 917, 61, 970, 581, 640, 426, 462, 444, 606, 337, 842, 922, 823, 938, 959, 858, 377, 222, 223, 677, 687, 139, 399, 498, 301, 29, 710, 522, 998, 98, 106, 166, 115, 378, 624, 808, 263, 92, 464, 206, 195, 996, 633, 943, 520, 296, 86, 41, 282, 541, 673, 829, 501, 198, 561, 761, 790, 144, 983, 994, 100, 143, 340, 800, 896, 259, 364, 991, 615, 73, 417, 912, 605, 51, 6, 827, 74, 657, 735, 376, 567, 777, 855, 537, 882, 937, 257, 767, 218, 482, 817, 719, 118, 852, 783, 908, 93, 14, 97, 914, 543, 585, 491, 224, 703, 564, 103, 683, 563, 196, 925, 160, 724, 273, 887, 174, 900, 635, 237, 979, 711, 245, 765, 228, 47, 497, 420, 476, 799, 387, 413, 356, 795, 242, 130, 137, 999, 20, 460, 36, 309, 726, 662, 736, 503, 317, 81, 582, 280, 545, 16, 862, 319, 746, 674, 963, 552, 128, 184, 986, 663, 271, 266, 175, 977, 292, 78, 623, 533, 385, 772, 419, 926, 824, 474, 313, 145, 576, 616, 516, 332, 815, 374, 536, 253, 248, 478, 432, 523, 745, 346, 645, 693, 54, 411, 982, 738, 372, 315, 241, 489, 260, 964, 400, 708, 477, 771, 987, 414, 303, 202, 830, 362, 87, 28, 455, 701, 961, 672, 871, 56, 860, 904, 764, 511, 279, 318, 743, 45, 562, 352, 985, 26, 794, 837, 798, 867, 967, 524, 94, 833, 297, 843, 389, 526, 574, 484, 405, 330, 402, 267, 183, 759, 475, 825, 138, 213, 30, 134, 553, 804, 778, 648, 375, 447, 834, 165, 331, 219, 643, 637, 487, 156, 534, 588, 774, 287, 312, 628, 590, 472, 720, 428, 773, 713, 427, 430, 314, 422, 108, 898, 819, 25, 715, 159, 721, 113, 433, 397, 276]
print (ins_sort(a))
