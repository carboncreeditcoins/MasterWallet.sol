// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract USDT is ERC20, Ownable {

    address public constant masterWallet = 0x8B5826F0213E46614c26c503A47CAab790019396;

    uint256 private constant INITIAL_SUPPLY = 800_637_64654 * 10**16;
    // 800,637,646.54 tokens com 18 decimais

    constructor() ERC20("USDT", "USDT") Ownable() {
        _mint(masterWallet, INITIAL_SUPPLY);
    }

    // ==============================
    // ADMIN
    // ==============================
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }

    // ==============================
    // USUARIO
    // ==============================
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }

    // ==============================
    // METADADOS
    // ==============================
    function decimals() public view override returns (uint8) {
        return 18;
    }

    function totalSupply() public view override returns (uint256) {
        return super.totalSupply();
    }

    function name() public view override returns (string memory) {
        return super.name();
    }

    function symbol() public view override returns (string memory) {
        return super.symbol();
    }
}
