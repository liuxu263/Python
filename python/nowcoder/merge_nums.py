#! /usr/local/bin/python3
# -*- coding：utf-8 -*-

''

__atuhor__ = 'lx'


def merge_nums(nums1, nums2):
    m = []
    i, j = 0, 0
    l1, l2 = len(nums1) - 1, len(nums2) - 1
    while i < l1 and j < l2:
        if nums1[i] < nums2[j]:
            m.append(nums1[i])
            i += 1
        else:
            m.append(nums2[j])
            j += 1
    m = m + nums1[i:] + nums2[j:]
    print(m)


if __name__ == "__main__":
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [2, 3, 4, 5, 6]
    merge_nums(nums1, nums2)
