import 'package:flutter/material.dart';

class ClayCard extends StatelessWidget {
  const ClayCard({super.key, this.onPressed});

  final VoidCallback? onPressed;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        color: const Color(0xFFCFD4FF),
        borderRadius: BorderRadius.circular(32),
        boxShadow: const [
          BoxShadow(color: Color(0x3E52425B), offset: Offset(0, 18), blurRadius: 28),
          BoxShadow(color: Color(0x80FFFFFF), offset: Offset(0, -5), blurRadius: 12),
        ],
      ),
      child: FilledButton(
        onPressed: onPressed,
        style: FilledButton.styleFrom(
          minimumSize: const Size(44, 44),
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
        ),
        child: const Text('Start'),
      ),
    );
  }
}
