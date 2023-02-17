#include <iostream>
#include <vector>

using namespace std;

int binary_search_helper(vector<int> nums, int target, int l, int r){
    /*

    l = 0, r= len

    get mid, 
    if the element == mid return 

    if less,
    r = m

    if more,
    l = m

    */
    if (r >= l){

        int mid =  l + (r - l)/2;

        if (target == nums[mid]){
            return mid;
        }
        else if (target > nums[mid]){
            return binary_search_helper(nums, target, mid+1, r);
        }
        else{
            return binary_search_helper(nums, target, l, mid-1);
        }
    
    }
    return -1;

    
}

int binary_search(vector<int> nums, int target){
    int l = 0;
    int r = nums.size()-1;
    return binary_search_helper(nums, target, l, r);
}


int main(){

    vector<int> nums;
    for (int i=0;i<10;i++){
        nums.push_back(i);
    }

    int target = 18;

    cout<<binary_search(nums, target)<<endl;

    return 0;
}