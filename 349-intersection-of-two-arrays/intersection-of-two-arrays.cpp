class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        vector<int> res;

        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());

        int i = 0;
        int j = 0;

        while (i < nums1.size() && j < nums2.size()) {
            int n1 = nums1[i];
            int n2 = nums2[j];
            if (n1 == n2) {
                if (res.empty() || res.back() != n1) {
                    res.push_back(n1);
                } 
                ++i;
                ++j;
            }
            else if (n1 < n2) {
                i++;
            }
            else {
                j++;
            }
        }

        return res;
    }
};