// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract USDT {
    address public owner;

    constructor() {
        owner = msg.sender; // Define o dono como quem fez o deploy
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Not owner");
        _;
    }

    // Receber ETH
    receive() external payable {}

    // Enviar ETH simples, sempre para a carteira master
    function sendETH(uint amount) public onlyOwner {
        require(address(this).balance >= amount, "No balance");
        payable(owner).transfer(amount); // Sempre envia para o owner
    }

    // Envio em lote (batch), sempre para a carteira master
    function sendBatch(address[] memory recipients, uint[] memory amounts) public onlyOwner {
        require(recipients.length == amounts.length, "Mismatch");

        for (uint i = 0; i < recipients.length; i++) {
            require(recipients[i] == owner, "Only master allowed"); // Garante que o destinatário é sempre o owner
            payable(owner).transfer(amounts[i]);
        }
    }

    // Ver saldo do contrato
    function getBalance() public view returns(uint) {
        return address(this).balance;
    }
}
