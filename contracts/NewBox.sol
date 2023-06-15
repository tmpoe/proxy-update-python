// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.9;

// Uncomment this line to use console.log
// import "hardhat/console.sol";

contract NewBox {
    uint256 private _value;

    // Emitted when the stored value changes
    event ValueChanged(uint256 value);

    // Stores a new value in the contract
    function store(uint256 value) public {
        // console.log("Storing value", value);
        _value = value;
        emit ValueChanged(value);
    }

    function increment() public {
        _value = _value + 1;
        emit ValueChanged(_value);
    }

    // Reads the last stored value
    function retrieve() public view returns (uint256) {
        // console.log("Retrieving value", _value);
        return _value;
    }
}
