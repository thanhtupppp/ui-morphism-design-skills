import 'dart:ui';
import 'package:flutter/material.dart';

class LiquidGlassToolbar extends StatelessWidget {
  const LiquidGlassToolbar({super.key});

  @override
  Widget build(BuildContext context) {
    return ClipRRect(
      borderRadius: BorderRadius.circular(999),
      child: BackdropFilter(
        filter: ImageFilter.blur(sigmaX: 20, sigmaY: 20),
        child: Container(
          padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
          decoration: BoxDecoration(
            color: const Color(0x9EFFFFFF),
            border: Border.all(color: const Color(0xB8FFFFFF)),
            borderRadius: BorderRadius.circular(999),
          ),
          child: Row(
            mainAxisSize: MainAxisSize.min,
            children: [
              IconButton(tooltip: 'Search', onPressed: () {}, icon: const Icon(Icons.search)),
              IconButton(tooltip: 'Settings', onPressed: () {}, icon: const Icon(Icons.settings)),
            ],
          ),
        ),
      ),
    );
  }
}
