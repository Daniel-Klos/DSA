class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        vector<int> res;

        set<int> s1(nums1.begin(), nums1.end());
        set<int> s2(nums2.begin(), nums2.end());
        for (int elem : s1) {
            if (s2.contains(elem)) {
                res.push_back(elem);
            }
        }

        return res;
    }
};